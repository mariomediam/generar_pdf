export const getUserbyId = async (id) => {
  const url = `http://localhost:8085/${id}`;
  const resp = await fetch(url);
  const { data } = await resp.json();

  return data;
};

export const getPdfUserbyId = async (id) => {
  const response = await fetch(`http://localhost:8085/pdf/${id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/pdf",
    },
  });

  return response;
};

export const getTestUser = async () => {
    const response = await fetch(`http://localhost:8085/list`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const { content } = await response.json();
  
      return content;
};
