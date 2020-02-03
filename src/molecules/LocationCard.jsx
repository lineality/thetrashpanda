import React from "react";

import styled from "styled-components";

const Container = styled.div`
  padding: 8px 12px;
  border: 0.5px solid #d9d9d9;
  box-sizing: border-box;
  border-radius: 5px;

  margin: 30px 16px;
`;

const Title = styled.h2`
  font-family: Muli;
  font-style: normal;
  font-weight: bold;
  font-size: 15px;
  color: #404040;

  text-decoration-line: underline;
  margin: 0;
  padding: 0;
`;

const PText = styled.p`
  color: #404040;
  font-family: Muli;
  font-style: normal;
  font-weight: normal;
  font-size: 15px;

  margin: 0px;
`;

const FlexContainer = styled.div`
  display: flex;
  justify-content: space-between;
`;

const Address = styled.div`
  width: 100px;

  margin-top: 9px;
  margin-bottom: 8px;
`;

const Hours = styled.div`
  margin-bottom: 16px;
  margin-top: 8px;
`;
const LocationCard = ({ title, address, hours, phone }) => {
  return (
    <Container>
      <Title>{title}</Title>
      <FlexContainer>
        <Address>
          <PText>{address}</PText>
        </Address>
        <div>
          <Hours>
            <PText>Hours: {hours}</PText>
          </Hours>
          <PText>Phone: {phone}</PText>
        </div>
      </FlexContainer>
    </Container>
  );
};

export default LocationCard;
