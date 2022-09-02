// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import React from 'react';
import { Container, Row, Col } from 'reactstrap';

const Hero = () => {
  return (
    <section className="section position-relative">
      <Container>
        <Row className="align-items-center">
          <Col lg={6}>
            <div className="pr-lg-5">
              <p className="text-uppercase text-primary font-weight-medium f-14 mb-4">pronounced as <strong>Link Shortener</strong></p>
              <h1 className="mb-4 font-weight-normal line-height-1_4">A no-BS URL Shortening Service! <span className="text-primary font-weight-medium">lnq-shortr</span></h1>
              <p className="text-muted mb-4 pb-2">lnq-shortener intends to be a minimalistic, fast and reliable URL shortening service. Currently in beta free for all users <em>(with generous limits of course!).</em>.</p>
              <a href="#" className="btn btn-warning">
                Sign Up Now! <span className="ml-2 right-icon">&#8594;</span>
              </a>
            </div>
          </Col>
          <Col lg={6}>
            <div className="mt-5 mt-lg-0">
              <img src="/images/Group Members.png" alt="" className="img-fluid mx-auto d-block"/>
            </div>
          </Col>
        </Row>
      </Container>
    </section>
  );
}

export default Hero;