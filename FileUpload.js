import React, { useState } from "react";
import axios from "axios";

const FileUpload = ({ onUploadComplete }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      // Send the file to the Flask backend
      const response = await axios.post(
        "http://localhost:5000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      // Log the entire response data to inspect it
      console.log("Response data received from Flask:", response.data);

      // Ensure response.data is an array
      let data = response.data;

      if (data && !Array.isArray(data)) {
        console.error("Data is not an array. Trying to extract records.");
        data = data.data || data.records || []; // Adjust based on response structure
      }

      // Ensure valid data array
      if (Array.isArray(data) && data.length > 0) {
        console.log("Valid data array received:", data);
        onUploadComplete(data); // Send data to parent
      } else {
        alert("Error: Data is not in the expected format.");
        console.error("Invalid data format:", data);
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Failed to upload the file.");
    }
  };

  return (
    <div>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default FileUpload;
