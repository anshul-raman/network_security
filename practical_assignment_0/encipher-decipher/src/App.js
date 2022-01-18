import { useState } from "react";
import { encAlgoNames, encAlgos } from "./utils/encryption";

function App() {
  const [orignalText, setOrignalText] = useState("");
  const [encText, setEncText] = useState("");
  const [currentEncAlgo, setCurrentEncAlgo] = useState("Atbash");

  const handleOrignalText = (text) => {
    let encFunction = (t) => t;
    if (currentEncAlgo in encAlgos) {
      if ("encrypt" in encAlgos[currentEncAlgo]) {
        encFunction = encAlgos[currentEncAlgo].encrypt;
      }
    }

    setOrignalText(text);
    setEncText(encFunction(text));
  };

  const handleEncText = (text) => {
    let decFunction = (t) => t;
    if (currentEncAlgo in encAlgos) {
      if ("decrypt" in encAlgos[currentEncAlgo]) {
        decFunction = encAlgos[currentEncAlgo].decrypt;
      }
    }

    setEncText(text);
    setOrignalText(decFunction(text));
  };

  return (
    <div className="bg-blue-100 w-screen h-screen flex">
      <div className=" bg-violet-700 shadow-violet-700 shadow-2xl rounded-lg p-7 mx-auto my-auto">
        {/* main container with two input box  */}
        <div className=" flex gap-5 ">
          <div>
            <p className="my-2 text-2xl text-indigo-50">Orignal Text</p>
            <textarea
              value={orignalText}
              onChange={(e) => handleOrignalText(e.target.value)}
              className=" focus:outline-none  rounded resize-none h-60 w-60 p-5"
            />
          </div>

          <div>
            <p className="my-2 text-2xl text-indigo-50"> Encrypted text</p>
            <textarea
              // readOnly={true}
              value={encText}
              onChange={(e) => handleEncText(e.target.value)}
              className="rounded focus:outline-none resize-none h-60 w-60 p-5"
            />
          </div>
        </div>

        <div>
          <select
            className="outline-none p-3 my-4 shadow-md text-indigo-50  bg-purple-600 rounded-md"
            onChange={(event) => {
              setCurrentEncAlgo(event.target.value);
            }}
          >
            {encAlgoNames.map((name, idx) => (
              <option
                className="p-3 text-indigo-50 bg-purple-600"
                key={name}
                value={name}
              >
                {name}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
}

export default App;
