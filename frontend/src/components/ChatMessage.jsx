// src/components/ChatMessage.jsx
import React from 'react';

export default function ChatMessage({ message }) {
  return (
    <div className={`message ${message.isBot ? 'bot' : 'user'}`}>
      {message.text}
    </div>
  );
}