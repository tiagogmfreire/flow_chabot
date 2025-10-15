// src/components/ChatBot.jsx
import React, { useState } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';

export default function ChatBot() {
  const [messages, setMessages] = useState([
    { text: "Hi! How can I help you today?", isBot: true }
  ]);

  const handleSendMessage = (message) => {
    // Add user message
    setMessages(prev => [...prev, { text: message, isBot: false }]);
    
    // Simulate bot response (replace with actual API call later)
    setTimeout(() => {
      setMessages(prev => [...prev, { 
        text: `I received: "${message}"`, 
        isBot: true 
      }]);
    }, 1000);
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}
      </div>
      <ChatInput onSendMessage={handleSendMessage} />
    </div>
  );
}