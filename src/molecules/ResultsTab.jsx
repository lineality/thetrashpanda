import React, { useState, useEffect } from "react";
import styled from "styled-components";
import Button from "../atoms/Button";

import { useHistory } from "react-router-dom";

const Container = styled.div`
    max-width= 575px;
    width: 100%;
    position:absolute;
    bottom: 0;
    display: flex;
    justify-content: space-evenly;
    align-items: center;

`;

const ResultsBox = styled.div`
  width: 98vw;
  background-color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 15px 15px 0px 0px;
  transition: height 4s;

  &:hover {
    height: 500px;
  }
`;

const ResultsTab = () => {
  const [result, setResult] = useState("");
  const history = useHistory();

  const handleSearchReturn = () => {
    history.push(`/`);
  };

  return (
    <Container>
      {result === "" ? (
        <ResultsBox>
          <p>No results found</p>
          <p>1</p>
          <p>2</p>
          <p>3</p>
          <Button>Search</Button>
        </ResultsBox>
      ) : (
        <ResultsBox>
          <p>Is this an</p>
          {result}
          <p>1</p>
          <p>2</p>
          <p>3</p>
        </ResultsBox>
      )}
    </Container>
  );
};

export default ResultsTab;
