// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import React from 'react';
import { Container, Row, Col } from "reactstrap";

const currentYear = new Date().getFullYear();

const Footer = () => {
  const links = [
    
    { id : 2, title : "About Us",
      child : [
          { title : "FAQs", link : "/faq" },
          { title : "Privacy Policy", link : "/privacy" },
      ]
    },
  ];
  
  return (
    <section className="footer section">
      <Container>
        <Row>
  
          <Col lg={12}>           
            <Row>
              {
                links.map((link, key) =>
                  <Col key={key} md={6}>
                    <h6 className="text-dark mb-3">{link.title}</h6>
                    <ul className="list-unstyled company-sub-menu">
                      {
                        link.child.map((fLink, key) =>
                          <li key={key}><a href={fLink.link}>{fLink.title}</a></li>
                        )
                      }
                    </ul>
                  </Col>
                )
              }
              
              <Col md={6}>
                <h6 className="text-dark mb-3">Our Address</h6>
                <p className="text-muted f-14">Mumbai, MH, 🇮🇳</p>
                <h6 className="text-muted pb-2">Email: support[at]lnqshortr.com</h6>
                <ul className="list-unstyled footer-social-list mt-4">
                  <li className="list-inline-item"><a href="#"><i className="mdi mdi-facebook"></i></a></li>
                  <li className="list-inline-item"><a href="#"><i className="mdi mdi-instagram"></i></a></li>
                  <li className="list-inline-item"><a href="#"><i className="mdi mdi-linkedin"></i></a></li>
                </ul>
              </Col>
            </Row>
          </Col>
        </Row>
         

        <Row className="mt-5">
          <Col md={12}>
            <div className="text-center text-muted">
              <p className="mb-0 f-15">{currentYear} © lnq-shortr by <a href="https://nikhilakki.in/about" target="__blank">Nikhil Akki</a></p>
            </div>
          </Col>
        </Row>
      </Container>
    </section>
  );
}

export default Footer;