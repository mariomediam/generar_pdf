import { useEffect, useState } from "react";
import { getPdfUserbyId, getTestUser } from "./helpers/testUser";

export const DownloadPdf = () => {
  const [listUser, setListUser] = useState([]);

  const downloadPdf = async (e) => {
    e.preventDefault();
    const userId = e.target.elements.userId.value;
    const response = await getPdfUserbyId(userId);

    const blob = await response.blob();
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = `userId-${userId}.pdf`;
    link.click();
  };

  const testUserList = async () => {
    const data = await getTestUser();
    setListUser(data);
  };

  useEffect(() => {
    testUserList();
  }, []);

  return (
    <>
      <h1>Descargar PDF desde Django</h1>

      <p>Usuarios:</p>

      <ul>        
        {listUser.map((user) => (
          <li className="text-ali" key={user.testUserId}>
            id {user.testUserId} - {user.testUserName}
          </li>
        ))}
      </ul>
      <p>Ingrese id para descargar PDF</p>

      <form onSubmit={downloadPdf}>
        <input type="text" placeholder="Ingrese id" name="userId" />
        <button type="submit">Download</button>
      </form>
    </>
  );
};
