import React, { useState } from "react";
import ReactDOM from "react-dom";
import styled from "styled-components";

import "./login.css";

export default function Login() {
  // React States
  const [errorMessages, setErrorMessages] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  // User Login info
  // Get data from table
  const database = [
    {
      username: "user1",
      password: "pass1",
    },
    {
      username: "user2",
      password: "pass2",
    },
  ];

  const errors = {
    uname: "invalid username",
    pass: "invalid password",
  };

  const handleSubmit = (event) => {
    //Prevent page reload
    event.preventDefault();

    var { uname, pass } = document.forms[0];

    // Find user login info
    const userData = database.find((user) => user.username === uname.value);

    // Compare user info
    if (userData) {
      if (userData.password !== pass.value) {
        // Invalid password
        setErrorMessages({ name: "pass", message: errors.pass });
      } else {
        setIsSubmitted(true);
      }
    } else {
      // Username not found
      setErrorMessages({ name: "uname", message: errors.uname });
    }
  };

  // Generate JSX code for error message
  const renderErrorMessage = (name) =>
    name === errorMessages.name && (
      <div className="error">{errorMessages.message}</div>
    );

  // JSX code for login form
  const renderForm = (
    <>
      <Wrapper onSubmit={handleSubmit}>
        <h2> Sign In </h2>
        <Spacer size={20} />
        <Field>
          <label>Username </label>
          <input type="text" name="uname" required />
          {renderErrorMessage("uname")}
        </Field>
        <Field>
          <label>Password </label>
          <input type="password" name="pass" required />
          {renderErrorMessage("pass")}
        </Field>
        <Spacer size={20} />
        <button type="submit">Sign In</button>
      </Wrapper>
    </>
  );

  return (
    <>{isSubmitted ? <div>User is successfully logged in</div> : renderForm}</>
    // <div className="app">
    //   <div className="login-form">
    //     <div className="title">Sign In</div>
    //     {isSubmitted ? <div>User is successfully logged in</div> : renderForm}
    //   </div>
    // </div>
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

const Field = styled.div`
  padding-top: 15px;
  display: flex;
  flex-direction: column;

  input {
    padding: 8px;
    border: none;
    border-radius: 5px;
    box-shadow: var(--shadow-elevation-medium);
  }

  label {
    padding-bottom: 5px;
    text-transform: uppercase;
    font-size: 0.6rem;
    color: var(--gray-300);
  }
`;
