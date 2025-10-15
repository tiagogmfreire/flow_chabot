// src/components/ChatMessage.jsx
import React from 'react';

export default function ChatMessage({ message }) {
  return (
    <div 
      className={`max-w-[80%] px-3 py-2 mb-2 rounded-2xl break-words ${
        message.isBot 
          ? "self-start bg-gray-100 text-gray-800" 
          : "self-end bg-blue-500 text-white"
      }`}
    >
      {message.text}
    </div>
  );
}