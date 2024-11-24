import React from "react";

const DataTable = ({ data }) => {
  // Check if data is an array before calling .map()
  if (!Array.isArray(data)) {
    return <p>No data available or invalid data format.</p>;
  }

  if (data.length === 0) return <p>No data to display</p>;

  const columns = Object.keys(data[0]); // Extract column names dynamically

  return (
    <table border="1">
      <thead>
        <tr>
          {columns.map((col) => (
            <th key={col}>{col}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            {columns.map((col) => (
              <td key={col}>{row[col]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DataTable;
