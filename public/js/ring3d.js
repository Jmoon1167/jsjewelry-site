// Homepage hero: real-time 3D gold solitaire with pavé shoulders, gold dust and sparkles.
// Progressive enhancement: the hero photo stays visible unless WebGL is available and
// the visitor hasn't asked for reduced motion.
const stage = document.querySelector('.hero-3d');
const reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

function webglOK() {
  try {
    const c = document.createElement('canvas');
    return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')));
  } catch (e) { return false; }
}

if (stage && !reduce && webglOK()) {
  Promise.all([
    import('./vendor/three.module.min.js'),
    import('./vendor/RoomEnvironment.js'),
  ]).then(([THREE, { RoomEnvironment }]) => init(THREE, RoomEnvironment))
    .catch(() => { /* keep the photo */ });
}

function init(THREE, RoomEnvironment) {
  const canvas = document.createElement('canvas');
  canvas.className = 'ring3d';
  canvas.setAttribute('aria-hidden', 'true');
  stage.appendChild(canvas);

  const small = window.innerWidth < 700;
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, small ? 1.75 : 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.outputColorSpace = THREE.SRGBColorSpace;

  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.035).texture;

  // Stones get their own high-contrast "studio": bright with scattered dark and hot
  // panels, so facets flip between white and black the way a real diamond does.
  const studio = new THREE.Scene();
  studio.background = new THREE.Color(0xb9bac2);
  const strip = new THREE.PlaneGeometry(1, 1);
  for (let i = 0; i < 70; i++) {
    const kind = i % 3;                   // 0 dark, 1 hot white, 2 warm
    const m = new THREE.Mesh(strip, new THREE.MeshBasicMaterial({
      color: kind === 0 ? 0x0a0a0d : kind === 1 ? 0xffffff : 0xffe2b0, side: THREE.DoubleSide,
    }));
    if (kind) m.material.color.multiplyScalar(kind === 1 ? 6 : 3);
    const th = Math.random() * Math.PI * 2, ph = Math.acos(2 * Math.random() - 1);
    m.position.setFromSphericalCoords(6, ph, th);
    m.lookAt(0, 0, 0);
    m.scale.set(0.6 + Math.random() * 2.2, 0.3 + Math.random() * 0.9, 1);
    studio.add(m);
  }
  const studioEnv = pmrem.fromScene(studio, 0).texture;

  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 100);
  camera.position.set(0, 0.35, 7.2);
  camera.lookAt(0, 0.25, 0);

  // Warm key and cool rim so the gold reads warm and the stone stays white
  const key = new THREE.PointLight(0xffe2a8, 40, 30); key.position.set(3, 4, 5); scene.add(key);
  const rim = new THREE.PointLight(0xcfe0ff, 25, 30); rim.position.set(-4, 2, -3); scene.add(rim);

  // ---------- Materials ----------
  const gold = new THREE.MeshPhysicalMaterial({
    color: 0xe7b85a, metalness: 1, roughness: 0.16, clearcoat: 0.4, clearcoatRoughness: 0.08, envMapIntensity: 1.25,
  });
  const diamond = new THREE.MeshPhysicalMaterial({
    color: 0xffffff, metalness: 1, roughness: 0, envMap: studioEnv, envMapIntensity: 1.1, flatShading: true,
    iridescence: 0.85, iridescenceIOR: 2.1, iridescenceThicknessRange: [200, 700],
  });

  // ---------- Ring ----------
  const ring = new THREE.Group();
  const R = 1.05;                         // inner-ish radius of the band

  // Comfort-fit shank: torus with a slightly flattened, wider-than-tall profile
  const shank = new THREE.Mesh(new THREE.TorusGeometry(R, 0.085, 48, 220), gold);
  shank.scale.set(1, 1, 1.55);
  ring.add(shank);

  // Round brilliant: lathe profile with few radial segments -> visible facets
  const brilliant = (r) => {
    const pts = [
      new THREE.Vector2(0.0001, -r * 0.86), // culet
      new THREE.Vector2(r * 0.62, -r * 0.42),
      new THREE.Vector2(r * 1.0, -r * 0.04), // pavilion to girdle
      new THREE.Vector2(r * 1.0, r * 0.02),  // girdle
      new THREE.Vector2(r * 0.8, r * 0.2),
      new THREE.Vector2(r * 0.55, r * 0.32), // crown to table
      new THREE.Vector2(0.0001, r * 0.32),   // table
    ];
    const g = new THREE.LatheGeometry(pts, 16);
    g.computeVertexNormals();
    return g;
  };

  // Center stone and cathedral head
  const head = new THREE.Group();
  head.position.y = R + 0.36;
  const stoneR = 0.48;
  const stone = new THREE.Mesh(brilliant(stoneR), diamond);
  stone.position.y = 0.12;
  stone.rotation.y = Math.PI / 16;
  head.add(stone);

  // Gallery rail under the stone
  const rail = new THREE.Mesh(new THREE.TorusGeometry(stoneR * 0.72, 0.028, 16, 64), gold);
  rail.rotation.x = Math.PI / 2;
  rail.position.y = -0.12;
  head.add(rail);

  // Four claw prongs, curving over the girdle
  for (let i = 0; i < 4; i++) {
    const a = Math.PI / 4 + i * Math.PI / 2;
    const curve = new THREE.CatmullRomCurve3([
      new THREE.Vector3(Math.cos(a) * 0.14, -0.40, Math.sin(a) * 0.14),
      new THREE.Vector3(Math.cos(a) * 0.36, -0.14, Math.sin(a) * 0.36),
      new THREE.Vector3(Math.cos(a) * (stoneR + 0.035), 0.12, Math.sin(a) * (stoneR + 0.035)),
      new THREE.Vector3(Math.cos(a) * (stoneR - 0.06), 0.21, Math.sin(a) * (stoneR - 0.06)),
    ]);
    const prong = new THREE.Mesh(new THREE.TubeGeometry(curve, 24, 0.032, 10, false), gold);
    head.add(prong);
    const tip = new THREE.Mesh(new THREE.SphereGeometry(0.042, 12, 10), gold);
    tip.position.copy(curve.getPoint(1));
    head.add(tip);
  }
  ring.add(head);

  // Pavé along the upper shoulders of the band
  const pave = [];
  const paveCount = 22;
  const paveGeo = brilliant(0.055);
  const paveMesh = new THREE.InstancedMesh(paveGeo, diamond, paveCount * 2);
  const m4 = new THREE.Matrix4(), q = new THREE.Quaternion(), s = new THREE.Vector3(1, 1, 1);
  const up = new THREE.Vector3(0, 1, 0);
  let k = 0;
  for (const side of [-1, 1]) {
    for (let i = 0; i < paveCount; i++) {
      const t = 0.32 + i * 0.052;         // radians from top, skipping under the head
      const ang = Math.PI / 2 + side * t;
      const n = new THREE.Vector3(Math.cos(ang), Math.sin(ang), 0);
      const p = n.clone().multiplyScalar(R + 0.075);
      q.setFromUnitVectors(up, n);
      m4.compose(p, q, s);
      paveMesh.setMatrixAt(k++, m4);
      pave.push(p);
    }
  }
  ring.add(paveMesh);

  ring.rotation.x = -0.32;
  ring.position.y = -0.05;
  scene.add(ring);

  // ---------- Gold dust ----------
  const dustN = small ? 140 : 280;
  const dustPos = new Float32Array(dustN * 3);
  const dustSeed = new Float32Array(dustN);
  for (let i = 0; i < dustN; i++) {
    const r = 1.6 + Math.random() * 2.6, th = Math.random() * Math.PI * 2;
    dustPos[i * 3] = Math.cos(th) * r;
    dustPos[i * 3 + 1] = (Math.random() - 0.5) * 4.6;
    dustPos[i * 3 + 2] = Math.sin(th) * r - 0.6;
    dustSeed[i] = Math.random();
  }
  const dustGeo = new THREE.BufferGeometry();
  dustGeo.setAttribute('position', new THREE.BufferAttribute(dustPos, 3));
  dustGeo.setAttribute('seed', new THREE.BufferAttribute(dustSeed, 1));
  const dustMat = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
    uniforms: { uTime: { value: 0 }, uScale: { value: renderer.getPixelRatio() } },
    vertexShader: `
      attribute float seed; uniform float uTime; uniform float uScale; varying float vA;
      void main(){
        vec3 p = position;
        p.y += mod(uTime*0.08*(0.4+seed) + seed*5.0, 4.6) - 2.3 - position.y*0.0;
        p.x += sin(uTime*0.4 + seed*12.0)*0.12;
        vec4 mv = modelViewMatrix * vec4(p,1.0);
        gl_Position = projectionMatrix * mv;
        gl_PointSize = (2.0 + seed*4.0) * uScale * (6.0 / -mv.z);
        vA = (0.25 + 0.75*abs(sin(uTime*(0.6+seed) + seed*30.0))) * smoothstep(2.3,1.2,abs(p.y));
      }`,
    fragmentShader: `
      varying float vA;
      void main(){
        float d = length(gl_PointCoord-0.5);
        float a = smoothstep(0.5,0.0,d);
        gl_FragColor = vec4(vec3(0.96,0.80,0.47)*a*vA, a*vA);
      }`,
  });
  const dust = new THREE.Points(dustGeo, dustMat);
  scene.add(dust);

  // ---------- Sparkles (4-point stars that flash on the stones) ----------
  const starTex = (() => {
    const c = document.createElement('canvas'); c.width = c.height = 128;
    const g = c.getContext('2d');
    const grd = g.createRadialGradient(64, 64, 0, 64, 64, 64);
    grd.addColorStop(0, 'rgba(255,255,255,1)'); grd.addColorStop(0.15, 'rgba(255,246,220,.7)'); grd.addColorStop(1, 'rgba(255,240,200,0)');
    g.fillStyle = grd; g.fillRect(0, 0, 128, 128);
    g.globalCompositeOperation = 'lighter';
    for (const [w, h] of [[128, 5], [5, 128]]) {
      const l = g.createLinearGradient(0, 0, w > h ? 128 : 0, w > h ? 0 : 128);
      l.addColorStop(0, 'rgba(255,255,255,0)'); l.addColorStop(0.5, 'rgba(255,255,255,1)'); l.addColorStop(1, 'rgba(255,255,255,0)');
      g.fillStyle = l; g.fillRect(64 - w / 2, 64 - h / 2, w, h);
    }
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
  })();
  const sparkles = [];
  const anchors = [
    ...[0, 1, 2, 3, 4, 5].map((i) => {
      const a = i * Math.PI / 3;
      return new THREE.Vector3(Math.cos(a) * stoneR * 0.55, head.position.y + 0.12 + stoneR * 0.3, Math.sin(a) * stoneR * 0.55);
    }),
    ...pave.filter((_, i) => i % 4 === 0),
  ];
  for (let i = 0; i < (small ? 5 : 8); i++) {
    const sp = new THREE.Sprite(new THREE.SpriteMaterial({
      map: starTex, color: 0xffffff, transparent: true, depthWrite: false, depthTest: false, blending: THREE.AdditiveBlending, opacity: 0,
    }));
    sp.userData = { anchor: anchors[(i * 3) % anchors.length], t0: Math.random() * 6, dur: 0.7 + Math.random() * 0.5 };
    ring.add(sp);
    sparkles.push(sp);
  }

  // ---------- Interaction ----------
  let spin = 0, vel = 0.0045, dragging = false, lastX = 0, tiltX = 0, tiltY = 0, targetTX = 0, targetTY = 0;
  stage.addEventListener('pointermove', (e) => {
    const r = stage.getBoundingClientRect();
    targetTY = ((e.clientX - r.left) / r.width - 0.5) * 0.5;
    targetTX = ((e.clientY - r.top) / r.height - 0.5) * 0.35;
    if (dragging) { const dx = e.clientX - lastX; lastX = e.clientX; vel = dx * 0.004; spin += dx * 0.01; }
  });
  stage.addEventListener('pointerdown', (e) => { dragging = true; lastX = e.clientX; stage.setPointerCapture(e.pointerId); stage.classList.add('grab'); });
  const end = () => { dragging = false; stage.classList.remove('grab'); };
  stage.addEventListener('pointerup', end);
  stage.addEventListener('pointercancel', end);
  stage.addEventListener('pointerleave', () => { targetTX = targetTY = 0; });

  // ---------- Sizing / visibility ----------
  function resize() {
    const w = stage.clientWidth, h = stage.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    // keep the whole ring in frame on narrow (portrait) stages
    camera.fov = w / h < 0.9 ? 34 : 30;
    camera.updateProjectionMatrix();
  }
  new ResizeObserver(resize).observe(stage);
  resize();

  let visible = true, running = false, raf = 0;
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; kick(); }, { threshold: 0.01 }).observe(stage);
  document.addEventListener('visibilitychange', kick);
  function kick() {
    const go = visible && !document.hidden;
    if (go && !running) { running = true; clock.getDelta(); raf = requestAnimationFrame(tick); }
    if (!go && running) { running = false; cancelAnimationFrame(raf); }
  }

  const clock = new THREE.Clock();
  let time = 0, shown = false;
  const v = new THREE.Vector3();
  function tick() {
    if (!running) return;
    raf = requestAnimationFrame(tick);
    const dt = Math.min(clock.getDelta(), 0.05);
    time += dt;

    if (!dragging) { vel += (0.0045 - vel) * 0.02; spin += vel * 60 * dt; }
    tiltX += (targetTX - tiltX) * 0.05;
    tiltY += (targetTY - tiltY) * 0.05;

    ring.rotation.y = spin + tiltY;
    ring.rotation.x = -0.32 + tiltX + Math.sin(time * 0.6) * 0.04;
    ring.position.y = -0.05 + Math.sin(time * 0.9) * 0.06;
    key.position.x = Math.cos(time * 0.35) * 4;
    key.position.z = 4 + Math.sin(time * 0.35) * 2;

    dustMat.uniforms.uTime.value = time;
    dust.rotation.y = time * 0.03;

    for (const sp of sparkles) {
      const d = sp.userData;
      const ph = ((time + d.t0) % 3.2) / d.dur;  // flash, then rest
      const a = ph < 1 ? Math.sin(ph * Math.PI) : 0;
      sp.material.opacity = a;
      sp.material.rotation = time * 0.8;
      const sc = 0.12 + a * 0.32;
      sp.scale.set(sc, sc, 1);
      sp.position.copy(d.anchor);
      if (ph >= 1 && ph < 1.05) d.anchor = anchors[Math.floor(Math.random() * anchors.length)];
      // only flash stones facing the camera
      v.copy(sp.position).applyMatrix4(ring.matrixWorld);
      if (v.z < -0.2) sp.material.opacity = 0;
    }

    renderer.render(scene, camera);
    if (!shown) { shown = true; stage.classList.add('is-3d'); }
  }
  kick();
}
