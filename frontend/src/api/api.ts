import type { FormData } from "../utils/validate";

interface SubmitResponse {
  filename: string;
}

const API_BASE_URL = import.meta.env.VITE_API_URL;

export const submitAccount = async (
  formData: FormData
): Promise<SubmitResponse> => {
  const response = await fetch(`${API_BASE_URL}/api/account`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  });

  if (!response.ok) {
    throw new Error("Failed to submit form");
  }

  return response.json();
};

export const getDownloadUrl = (filename: string): string => {
  return `${API_BASE_URL}/api/download/${filename}`;
};
