// src/components/ChatInput.jsx
import React, { useState } from 'react';

export default function ChatInput({ onSendMessage }) {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <form 
      className="flex p-2 border-t border-gray-200" 
      onSubmit={handleSubmit}
    >
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message..."
        className="flex-1 px-3 py-2 border border-gray-300 rounded-full mr-2 focus:outline-none focus:ring-2 focus:ring-blue-300"
      />
      <button 
        type="submit" 
        className="bg-blue-500 text-white border-none rounded-full px-4 py-2 hover:bg-blue-600 transition-colors cursor-pointer"
      >
        Send
      </button>
    </form>
  );
}