import * as ReactDOM from 'https://esm.sh/react-dom'
import React, { useState, useEffect, useRef, useMemo } from 'https://esm.sh/react'
import { Canvas, useFrame, useThree, extend } from 'https://esm.sh/@react-three/fiber'
import * as THREE from "https://esm.sh/three"
import { OrbitControls } from 'https://esm.sh/three/addons/controls/OrbitControls.js';

// https://codeworkshop.dev/blog/2020-04-03-adding-orbit-controls-to-react-three-fiber
extend({ OrbitControls });

function randInt(max) {
  return Math.floor(Math.random() * max);
}

function randFloat(min, max, decimals = 6) {
  const str = (Math.random() * (max - min) + min).toFixed(decimals);

  return parseFloat(str);
}


const Animation = ({ balls }) => {
  const [count, setCount] = useState(0)
  const [positions, setPositions] = useState([])
  const targetRef = useRef(null)
  const gridLen = 10
  const currTimeout = useRef(null)
  useEffect(() => {
    if (count > 0) setCount(0);
    throwBall(0);
    return () => clearTimeout(currTimeout.current);
  }, [balls]);

  const throwBall = (currentCount) => {
    if (currentCount > balls) return;
    const start = [randFloat(-3, 3), randFloat(-1, 1)];
    const end = [randFloat(-25, 25), randFloat(-1, 1)];

    const hit = end[0] >= -3 && end[0] <= 3
    setPositions((prev) => [...prev, { start, end, hit, id: crypto.randomUUID() }]);
    currTimeout.current = setTimeout(() => throwBall(currentCount + 1), 1);
  };
  const checkInOut = ([x, y]) => x >= x1 && x <= x2 && y >= y1 && y <= y2;



  return React.createElement('div', {},
    React.createElement('span', null, `Fired: ${positions.length}`),
                            
    React.createElement(Canvas, {
      style: {width: "100%", height: "80vh"}  
    },
    React.createElement(CameraControls),
    React.createElement("ambientLight"),
    React.createElement('pointLight', { position: [10, 10, 10] }),
    React.createElement(Box, { position: [-4, 0, 0], emitting: true }),
    React.createElement(Box, { ref: targetRef, position: [4, 0, 0] }),
    ...positions.map(pos => {

      return React.createElement(Line, {
        key: pos.id,
        startPos: [-3, ...pos.start],
        endPos: [3, ...pos.end],
        hit: pos.hit,
        targetRef
      })
    })
  )
)
}


const CameraControls = () => {
  // Get a reference to the Three.js Camera, and the canvas html element.
  // We need these to setup the OrbitControls component.
  // https://threejs.org/docs/#examples/en/controls/OrbitControls

  const {
    camera,
    gl: { domElement },
  } = useThree();

  // Ref to the controls, so that we can update them on every frame using useFrame
  const controls = useRef();

  useFrame((state) => controls.current.update());
  return React.createElement('orbitControls', { ref: controls, args: [camera, domElement] })
};

function Line(props) {
  const ref = useRef(null);
  const points = [
    new THREE.Vector3(...props.startPos),
    new THREE.Vector3(...props.endPos),
  ]
  const lineGeometry = useMemo(()=> {
    return new THREE.BufferGeometry().setFromPoints(points)
  }, [...props.startPos, ...props.endPos])
  
  return React.createElement('group', {
    ...props,
  },
    React.createElement('line', {
      ref,
      geometry: lineGeometry
    },
      React.createElement('lineBasicMaterial', {
        attach: "material", color: props.hit ? "red" : "blue", lineWidth: 500
      })
    )
  )
}
function Ball(props) {
  const ref = useRef(null)
  //   const geometry = new THREE.SphereGeometry( 15, 32, 16 );
  // const material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );
  // const sphere = new THREE.Mesh( geometry, material );
  // scene.add( sphere );
  return React.createElement('mesh', {
    ...props,
    ref
  },
    React.createElement('sphereGeometry', { args: [0.2, 32, 16] }),
    React.createElement('meshBasicMaterial', { color: props.emitting ? "hotpink" : "orange" }),
  )
}

function Box(props) {
  // This reference gives us direct access to the THREE.Mesh object
  const ref = React.useRef()
  // Hold state for hovered and clicked events
  const [hovered, hover] = React.useState(false)
  const [clicked, click] = React.useState(false)
  // Subscribe this component to the render-loop, rotate the mesh every frame
  useFrame((state, delta) => {
    if (props.emitting) {
      // console.log(state, delta)
      // console.log(state.raycaster)
    }
  })

  const state = useThree()
  // console.log('three state', state)

  // Return the view, these are regular Threejs elements expressed in JSX

  return React.createElement("mesh", {
    ...props,
    ref,
    onClick: e => click(!clicked),
    onPointerOver: e => hover(true),
    onPointerOut: e => hover(false)
  },
    React.createElement("boxGeometry", { args: [2, 6, 2] }),
    React.createElement("meshStandardMaterial", { color: props.emitting ? "orange" : "yellow" })
  );
}

export default Animation;