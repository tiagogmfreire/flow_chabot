// src/components/ChatBot.jsx
import React, { useState } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';

const api = import.meta.env.PUBLIC_API

export default function ChatBot() {
  const [messages, setMessages] = useState([
    { text: "Hi! How can I help you today?", isBot: true }
  ]);

    const handleSendMessage = async (message) => {
        // Add user message
        setMessages(prev => [...prev, { text: message, isBot: false }]);
        
        // Set loading state
        setMessages(prev => [...prev, { text: "...", isBot: true, loading: true }]);
        
        try {
            // Replace with your actual API endpoint
            const response = await fetch(`${api}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ "chat": message }),
            });
            
            const data = await response.json();

            // console.log(data);
            
            // Replace loading message with actual response
            setMessages(prev => 
                prev.map((msg, i) => 
                    i === prev.length - 1 ? { text: data.message, isBot: true } : msg
                )
            );
        } catch (error) {

            console.log(error);

            // Handle errors
            setMessages(prev => 
                prev.map((msg, i) => 
                    i === prev.length - 1 ? { text: "Sorry, I'm having trouble responding right now.", isBot: true } : msg
                )
            );
        }
    };

  return (
    <div className="w-7xl h-[500px] border border-gray-300 rounded-lg flex flex-col overflow-hidden">
      <div className="flex-1 overflow-y-auto p-4 flex flex-col">
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}
      </div>
      <ChatInput onSendMessage={handleSendMessage} />
    </div>
  );
}