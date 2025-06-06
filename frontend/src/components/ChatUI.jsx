import { useState } from "react";

export default function ChatUI() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    const res = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div>
      <h2>AI Assistant</h2>
      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={handleSubmit}>Ask</button>
      <h3>Response:</h3>
      <p>{response}</p>
    </div>
  );
}