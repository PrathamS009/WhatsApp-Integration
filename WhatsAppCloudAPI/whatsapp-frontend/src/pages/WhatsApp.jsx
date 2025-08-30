import { useState } from "react";

function WhatsAppPage() {
  const [number, setNumber] = useState("");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState("");

  const sendMessage = async () => {
    try {
      const res = await fetch("http://localhost:5000/api/whatsapp/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ number, message }),
      });
      const data = await res.json();
      setStatus(JSON.stringify(data));
    } catch (err) {
      setStatus("Error sending message");
    }
  };

  return (
    <div className="p-6 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">Send WhatsApp Message</h2>

      <input
        type="text"
        placeholder="Enter number with country code"
        value={number}
        onChange={(e) => setNumber(e.target.value)}
        className="w-full p-5 border rounded-lg mb-4 text-lg"
      />
      <br />
      <textarea
        placeholder="Enter your message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="w-full p-3 border rounded-lg mb-4 text-lg h-32"
      />

      <button
        onClick={sendMessage}
        className="w-full bg-green-600 text-white py-3 rounded-lg text-lg hover:bg-green-700 transition"
      >
        Send
      </button>

      <p className="mt-4 text-sm text-gray-600">{status}</p>
    </div>
  );
}

export default WhatsAppPage;
