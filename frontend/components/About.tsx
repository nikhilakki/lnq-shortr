// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import React from 'react';
import { Container, Row, Col } from "reactstrap";


const About = () => {

  return (
    <section className="section bg-light" id="about">
      <Container>
        <Row className="justify-content-center">
          <Col lg={6} md={8}>
            <div className="title text-center mb-5">
              <h3 className="font-weight-normal text-dark">About <span className="text-warning">LnQ Shortr</span></h3>
              <p className="text-muted">pronounced as <strong>Link Shortner</strong>. It is a no-BS URL shortening service with no frills. It does what it is supposed to - i.e. <strong>Shorten URL links!</strong></p>
            </div>
            <div className="title text-center mb-5">
            <h6 className="text-dark font-weight-light f-20 mb-3">Built with 💛 in 🇮🇳 for the 🌍</h6>
                </div>
          </Col>
        </Row>
      </Container>
    </section>
  );
}

export default About;