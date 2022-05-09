import Login from "./components/login.js";
import Register from "./components/register.js";
import styled from "styled-components";
import React, { useState } from "react";
import "./App.css";
import LoginForm from "./components/loginForm.js";

function App() {
  //   const [users, setUsers] = useState([]);

  //   function addUser(username) {
  //     const newUsers = [...users, username];
  //     setUsers(newUsers);
  //   }

  return (
    <Wrapper>
      <LoginForm />
      {/* <Login />
      <Register addUser={addUser} /> */}
    </Wrapper>
  );
}

const Wrapper = styled.div`
  height: 100%;
  background-color: var(--gray-300);
  display: grid;
  place-items: center;
`;

// function App() {
//   return (
//     <>
//       <div className="App">
//         <nav class="navbar navbar-expand-lg navbar-light bg-light">
//           <div class="container-fluid">
//             <a class="navbar-brand" href="#">
//               Netflix But Better
//             </a>
//             <button
//               class="navbar-toggler"
//               type="button"
//               data-bs-toggle="collapse"
//               data-bs-target="#navbarSupportedContent"
//               aria-controls="navbarSupportedContent"
//               aria-expanded="false"
//               aria-label="Toggle navigation"
//             >
//               <span class="navbar-toggler-icon"></span>
//             </button>
//             <div class="collapse navbar-collapse" id="navbarSupportedContent">
//               <ul class="navbar-nav me-auto mb-2 mb-lg-0">
//                 <li class="nav-item">
//                   <a class="nav-link active" aria-current="page" href="#">
//                     Home
//                   </a>
//                 </li>
//                 <li class="nav-item">
//                   <a class="nav-link" href="#">
//                     Link
//                   </a>
//                 </li>
//                 <li class="nav-item dropdown">
//                   <a
//                     class="nav-link dropdown-toggle"
//                     href="#"
//                     id="navbarDropdown"
//                     role="button"
//                     data-bs-toggle="dropdown"
//                     aria-expanded="false"
//                   >
//                     Dropdown
//                   </a>
//                   <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
//                     <li>
//                       <a class="dropdown-item" href="#">
//                         Action
//                       </a>
//                     </li>
//                     <li>
//                       <a class="dropdown-item" href="#">
//                         Another action
//                       </a>
//                     </li>
//                     <li>
//                       <hr class="dropdown-divider" />
//                     </li>
//                     <li>
//                       <a class="dropdown-item" href="#">
//                         Something else here
//                       </a>
//                     </li>
//                   </ul>
//                 </li>
//                 <li class="nav-item">
//                   <a class="nav-link disabled">Disabled</a>
//                 </li>
//               </ul>
//               <form class="d-flex">
//                 <input
//                   class="form-control me-2"
//                   type="search"
//                   placeholder="Search"
//                   aria-label="Search"
//                 />
//                 <button class="btn btn-outline-success" type="submit">
//                   Search
//                 </button>
//               </form>
//             </div>
//           </div>
//         </nav>
//       </div>
//     </>
//   );
// }

export default App;
