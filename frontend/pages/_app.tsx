import { MsalProvider } from '@azure/msal-react';
import { NextComponentType } from 'next';
import { AppProps } from 'next/app';
import { msalInstance } from '../services/msal';
import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <MsalProvider instance={msalInstance}>
      <Component {...pageProps} />
    </MsalProvider>
  );
}

export default MyApp;