import '../styles/globals.css';
import { MsalProvider } from '@azure/msal-react';
import { AppProps } from 'next/app';
import { msalInstance } from '../services/msal';


function MyApp({ Component, pageProps }: AppProps) {
  return (
    <MsalProvider instance={msalInstance}>
      <Component {...pageProps} />
    </MsalProvider>
  );
}

export default MyApp;