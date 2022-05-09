import React, { useState } from "react";
import styled from "styled-components";
import Login from "./login";
import Register from "./register";

export default function LoginForm() {
  const [isLogin, setIsLogin] = useState(false);
  const [isRegister, setIsRegister] = useState(false);
  const [users, setUsers] = useState([]);

  function addUser(username) {
    const newUsers = [...users, username];
    setUsers(newUsers);
  }

  function toggleSignIn() {
    setIsLogin = true;
  }

  function toggleRegister() {
    setIsRegister = true;
  }

  return (
    <Wrapper>
      <h1>Welcome to Netflix But Better</h1>
      <Spacer size={20} />
      {isLogin ? (
        <Login />
      ) : (
        <button display={!isLogin} onClick={toggleSignIn}>
          Sign in
        </button>
      )}
      <Spacer size={20} />
      {isRegister ? (
        <Register addUser={addUser} />
      ) : (
        <button display={!isRegister} onClick={toggleRegister}>
          Sign up
        </button>
      )}
    </Wrapper>
  );
}

const Spacer = styled.div`
  height: ${(p) => p.size}px;
`;

const Wrapper = styled.form`
  width: 300px;
  background-color: var(--gray-100);
  border-radius: 10px;
  padding: 20px;

  h2 {
    margin: 0;
    font-size: 1.8rem;
    color: var(--gray-400);
  }

  button {
    cursor: pointer;
    background-color: var(--gray-400);
    border: none;
    color: var(--gray-100);
    width: 100%;
    padding: 12px;
    border-radius: 8px;
    box-shadow: var(--shadow-elevation-medium);
  }
  button:disabled {
    background-color: var(--gray-200);
    cursor: not-allowed;
  }

  --shadow-color: 231deg 21% 9%;
  box-shadow: 0.3px 0.5px 0.8px hsl(var(--shadow-color) / 0.11),
    2px 3.9px 6px -0.1px hsl(var(--shadow-color) / 0.15),
    3.5px 7px 10.7px -0.3px hsl(var(--shadow-color) / 0.2),
    5.3px 10.6px 16.2px -0.4px hsl(var(--shadow-color) / 0.25),
    7.7px 15.3px 23.4px -0.5px hsl(var(--shadow-color) / 0.3),
    11px 22.1px 33.7px -0.6px hsl(var(--shadow-color) / 0.34),
    15.8px 31.5px 48.1px -0.8px hsl(var(--shadow-color) / 0.39),
    22.3px 44.5px 67.9px -0.9px hsl(var(--shadow-color) / 0.44);
`;
