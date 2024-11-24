from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Set maximum allowed file size to 1.3 GB (1.3 * 1024 * 1024 * 1024 bytes)
app.config['MAX_CONTENT_LENGTH'] = 1.3 * 1024 * 1024 * 1024  # 1.3 GB in bytes

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        # Log the saved file path
        print("File saved at:", file_path)

        # Process the file in chunks
        chunk_size = 100000  # Number of rows per chunk
        chunks_processed = 0
        results = []

        # Read the CSV file in chunks
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            # Log the chunk's first few rows to verify data
            print("Processing chunk:", chunk.head())

            # Add dummy prediction column for demonstration
            chunk['prediction'] = ['benign' if i %
                                   2 == 0 else 'DDoS' for i in range(len(chunk))]

            # Append first 10 rows of the chunk to results for demonstration
            results.append(chunk.head(10))

            # Increment chunk counter
            chunks_processed += 1

            # Optional: Stop after processing 5 chunks
            if chunks_processed == 5:
                break

        # Concatenate the results into a single DataFrame
        final_result = pd.concat(results)

        # Log the concatenated result (before conversion to JSON)
        print("Final DataFrame before conversion:", final_result.head())

        # Convert final result to JSON and ensure it's an array
        final_result_list = final_result.to_dict(orient='records')

        # Log the final result as an array of records
        print("Final result to be returned as JSON:", final_result_list)

        # Return the final result as JSON
        return jsonify(final_result_list)

    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File is too large. Try splitting it into smaller chunks."}), 413


@app.route('/')
def home():
    return "Flask backend is running!"


if __name__ == '__main__':
    app.run(debug=True)
