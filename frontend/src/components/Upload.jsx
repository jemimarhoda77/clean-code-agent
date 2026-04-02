import { useState } from "react";
import axios from "axios";

function Upload() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    const logs = text.split("\n").filter(line => line.trim() !== "");

    const res = await axios.post("/analyze", { logs });

    setResult(res.data);
  };

  return (
    <div>
      <h2>Paste Logs</h2>

      <textarea
        rows="10"
        cols="60"
        placeholder="Paste logs here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br />
      <button onClick={handleAnalyze}>Analyze</button>

      {result && (
        <div>
          <h3>Anomalies</h3>
          <ul>
            {result.anomalies.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>

          <h3>Clusters</h3>
          {Object.keys(result.clusters).map((c) => (
            <div key={c}>
              <h4>{c}</h4>
              <ul>
                {result.clusters[c].map((m, i) => (
                  <li key={i}>{m}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Upload;