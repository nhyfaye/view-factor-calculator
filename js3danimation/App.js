import React from 'https://esm.sh/react'
import Animation from "./Animation.js";
const App = () => {
  const [balls, setBalls] = React.useState(5000)
  return React.createElement(
    'div',
    {},
    React.createElement(Form, { balls, setBalls }),
    React.createElement(Animation, { balls }),
  );
};

const Form = ({ balls, setBalls }) => {

  const handleSubmit = () => {
    console.log(valX, valY)
  }

  return React.createElement(
    'form',
    null,
    // <label>...</label>
    React.createElement('div', null,
      React.createElement('label', { htmlFor: "balls" }, "X Value"),
      React.createElement('input', {
        id: "balls", name: "balls", type: "number", value: balls, onChange: (e) => setBalls(e.traget.value)
      }),

    ),
    React.createElement('button', {
      type: 'button',
      onClick: handleSubmit
    }, "Calculate")
  );
}
export default App