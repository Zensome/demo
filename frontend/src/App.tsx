import { useState } from "react";
import type { FormEvent } from "react";
import {
  validateForm,
  type FormData,
  type ValidationErrors,
} from "./utils/validate";
import { submitAccount, getDownloadUrl } from "./api/api";
import { downloadFile } from "./utils/download";

function App() {
  const [formData, setFormData] = useState<FormData>({
    name: "",
    email: "",
    password: "",
  });
  const [errors, setErrors] = useState<ValidationErrors>({});
  const [downloadUrl, setDownloadUrl] = useState<string>("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    const validationErrors = validateForm(formData);
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length > 0) return;

    try {
      const data = await submitAccount(formData);
      setDownloadUrl(data.filename);
      setFormData({ name: "", email: "", password: "" });
      setErrors({});
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  const handleDownload = async () => {
    if (!downloadUrl) return;
    await downloadFile(getDownloadUrl(downloadUrl), downloadUrl);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h1 className="text-2xl font-bold mb-2">Data Form</h1>
        <p className="text-sm text-gray-500 mb-4">
          Enter your info and submit to get a download link for your encrypted
          data.
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <input
              type="text"
              placeholder="Name"
              value={formData.name}
              onChange={(e) =>
                setFormData({ ...formData, name: e.target.value })
              }
              className="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.name && (
              <p className="text-red-500 text-sm mt-1">{errors.name}</p>
            )}
          </div>

          <div>
            <input
              type="email"
              placeholder="Email"
              value={formData.email}
              onChange={(e) =>
                setFormData({ ...formData, email: e.target.value })
              }
              className="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.email && (
              <p className="text-red-500 text-sm mt-1">{errors.email}</p>
            )}
          </div>

          <div>
            <input
              type="password"
              placeholder="Password"
              value={formData.password}
              onChange={(e) =>
                setFormData({ ...formData, password: e.target.value })
              }
              className="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.password && (
              <p className="text-red-500 text-sm mt-1">{errors.password}</p>
            )}
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition"
          >
            Submit
          </button>
        </form>

        {downloadUrl && (
          <div className="mt-4">
            <button
              onClick={handleDownload}
              className="text-blue-500 hover:underline cursor-pointer"
            >
              Download submitted data
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
