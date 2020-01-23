/*eslint-disable*/
import React from "react";

// reactstrap components
import { Container, Row, Nav, NavItem, NavLink } from "reactstrap";

class Footer extends React.Component {
  render() {
    return (
      <footer className="footer">
        <Container fluid>
          <Nav>
            <NavItem>
              <NavLink href="javascript:void(0)">Libra</NavLink>
            </NavItem>
          </Nav>
          <div className="copyright">Vipul Petkar</div>
        </Container>
      </footer>
    );
  }
}

export default Footer;
