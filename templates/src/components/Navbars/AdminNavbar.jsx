// nodejs library that concatenates classes
import classNames from "classnames";
import React from "react";
// reactstrap components
import {
  Container,
  Navbar,
  NavbarBrand,
  Nav,
} from "reactstrap";

class AdminNavbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      collapseOpen: false,
      modalSearch: false,
      color: "navbar-transparent"
    };
  }
  componentDidMount() {
    window.addEventListener("resize", this.updateColor);
  }
  componentWillUnmount() {
    window.removeEventListener("resize", this.updateColor);
  }


  render() {
    return (
      <>
        <Navbar
          className={classNames("navbar-absolute", this.state.color)}
          expand="lg"
        >
          <Container fluid>
            <div className="navbar-wrapper">
              <div
                className={classNames("navbar-toggle d-inline", {
                  toggled: this.props.sidebarOpened
                })}
              >
                <button
                  className="navbar-toggler"
                  type="button"
                  onClick={this.props.toggleSidebar}
                >
                  <span className="navbar-toggler-bar bar1" />
                  <span className="navbar-toggler-bar bar2" />
                  <span className="navbar-toggler-bar bar3" />
                </button>
              </div>
              <Nav className="ml-auto" navbar>
                <NavbarBrand href="#pablo" onClick={e => e.preventDefault()}>
                  <img
                    alt="Libra"
                    width="100px"
                    height="45px"
                    src={require("assets/img/LibrusLogo.png")}
                  />
                </NavbarBrand>
              </Nav>
            </div>
          </Container>
        </Navbar>
      </>
    );
  }
}

export default AdminNavbar;
