// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { PublicClientApplication, Configuration } from "@azure/msal-browser";

const clientId = process.env.NEXT_PUBLIC_AZURE_AD_CLIENT_ID || ""
const authority = `https://login.microsoftonline.com/${process.env.NEXT_PUBLIC_AZURE_AD_TENANT_ID}`
console.log({ clientId, authority })
const msalConfig: Configuration = {
    auth: {
        clientId: clientId,
        authority: authority,
        redirectUri: '/'
    }
}

const msalInstance = new PublicClientApplication(msalConfig)

export { msalInstance }