// src/components/FileUpload.jsx
import React, { useState } from 'react';

const api = import.meta.env.PUBLIC_API

// console.log(api);

export default function FileUpload({ onFileUpload }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    if (uploadedFile && uploadedFile.type === 'application/pdf') {
      setFile(uploadedFile);
    } else {
      alert('Please upload a valid PDF file.');
      setFile(null);
    }
  };

  const handleUpload = async () => {
    if (!file) return;

    // Create a FormData object to send the file
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`${api}/uploadfile`, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      alert(data.message || "File uploaded successfully!");
    } catch (error) {
      alert("File upload failed.");
    }

    // Reset the file state
    setFile(null);
  };

  return (
    <div className="flex flex-col p-4 border border-gray-300 rounded-lg">
      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        className="mb-2 border border-gray-300 rounded-md"
      />
      <button 
        onClick={handleUpload} 
        className="bg-blue-500 text-white border-none rounded-full px-4 py-2 hover:bg-blue-600 transition-colors cursor-pointer"
      >
        Upload PDF
      </button>
    </div>
  );
}