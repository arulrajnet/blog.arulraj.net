---
title: "No More Basic Auth : htpasswd with OAuth2 Proxy"
date: 2024-12-15 20:44:14
author: arul
category: Security
tags:
  - proxy
  - Traefik
  - APISix
  - nginx
slug: no-more-basic-auth-htpasswd-with-oauth2-proxy
disqus_identifier: no-more-basic-auth-htpasswd-with-oauth2-proxy
cover: /assets/images/basic-auth-oauth2-proxy-cover.png
color: gray
headline: "No More Basic Auth: htpasswd with OAuth2 Proxy"
status: draft
---

In this blog post we are going to see the how we can enable authentication based on htpasswd file using OAuth2 proxy. 

Before that lets discuss the problem with the htpasswd + basic authentication.  
## The problem

What is htpasswd file?

This file contains the finite number of users and password encrypted using bcrypt highly secure algorithm. The file is look like below. 

```
admin@mycompany.com:$2y$05$Npda/wcHOGrBKYgr9sNJo./O8KZbXQqwTrF0BcRxiS5Vr.P37zDJC
user@mycompany.com:$2y$05$crIQ3pU/dJi2T6c8IM1UNOXV6KlgxjvFBvJH2ZfmmhgRSS8qObZVu
another-user@mycompany.com:$2y$05$tQrvnJQgeroRwi8FJgHsUufUZpU3lrmoMMXC9xYZ9XA9Kno0iwDWy
```

Most of the time the htpasswd file is used along with the basic authentication. Basic authentication is nothing but sending base64 encoded username and password as Authorization header bearer token in every request. Server side its validated against the file. 

All the proxies supported this way

* [NGinx](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/)
* [HAProxy](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/authentication/basic-authentication/)
* [Traefik](https://doc.traefik.io/traefik/middlewares/http/basicauth/)
* [APISix](https://apisix.apache.org/docs/apisix/plugins/basic-auth/)
* [Caddy](https://caddyserver.com/docs/caddyfile/directives/basic_auth)
* [Envoy](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/basic_auth_filter.html)

Do you know, this is the most insecure way to do the authn due to the following reasons. 

* Plain Username and Password sends in every request. Yeah its Base64, But its decodable. 
	* Lack of session management. 
	* Password stored in client side cache as plain text, which can be exploited if the device is compromised.
	* Expose in logs like browser history, server logs etc.,
* There is no logout. 

You might also seen this in your legacy router

![[basic-auth-popup.png]]

## The objective

The htpasswd is perfect fit for the application has finite number of users. The application want to use the flexibility of htpasswd but without basic authentication. Then OAuth2-Proxy is perfectly fits in this use case. 

The OAuth2-Proxy creates cookie session on login and do further authentication using the cookie. The cookie has expiry and have the way to refresh the cookie in certain interval. Built-in support for CSRF token.
## The challenges

The basic authentication can be solved in many ways. Here we choose the off the shelf FOSS software [OAuth2-Proxy](https://github.com/oauth2-proxy/oauth2-proxy)

Here are the challenges in using OAuth2-proxy.

* As the name suggests, this primary focus of this application is for the OIDC/OAuth2 based authentication.
	* So by default this application expect **at least one OIDC provider has to be configured**. 
	* The `htpasswd` file based authentication is optional
* No support for external standalone login page
	* The built-in login page can be customized.  But its pure HTML. 
	* Suppose your application has **ReactJS based branded login page, it won't support by default.** 
## Solutions 

There is two flavor of solutions to solve the above.

* Dummy OAuth2 Provider + Built-in Login Page.
* Dummy OAuth2 Provider + Standalone Login page.

The OAuth2-Proxy can be run as a http proxy, which route the traffic to the upstream. In this case, the routing is handled by some well known proxy and OAuth2-Proxy act as a [forward-auth](https://doc.traefik.io/traefik/middlewares/http/forwardauth/). 
### with built-in login page

I am the big fan of Traefik Proxy. Their docker label based configuration is another level 🔥in CNCF. Here I have chosen traefik as reverse proxy in front of OAuth2. 

![[htpasswd-oauth2-proxy.drawio.png]]

The config of oauth2 proxy is look like

```bash
--client-id=dummy-client-id,
--client-secret=dummy-client-secret,
--cookie-expire=168h,
--cookie-name=_session,
--cookie-refresh=30m,
--cookie-secret=cbiGJkwts9Ye6XD2Pbt_L1jLcipIZBDMfMuqxDWRbeQ=,
--custom-sign-in-logo=https://avatars.githubusercontent.com/u/4029521?v=4,
--custom-templates-dir=/templates,
--cookie-secure=false,
--email-domain=*,
--footer=Powered by <a href='https://mycompany.com'>My Company</a>,
--htpasswd-file=/.htpasswd,
--http-address=0.0.0.0:4181,
--provider=google,
--proxy-prefix=/auth,
--reverse-proxy=true,
--set-authorization-header,
--set-xauthrequest,
--skip-provider-button=false,
--upstream=static://202
```

In this the client-id and client-secret are dummy values. 

The Login page

![[oauth2-proxy-login-page.png]]

The Cookie

![[oauth2-proxy-cookie-page.png]]

The docker compose stack is in [GitHub Repo](https://github.com/arulrajnet/oauth2-proxy-without-provider/tree/for-blog-post/built-in-login-page)
### with standalone login page

In some cases, the login page also serve from the application. This is for, how to handle it. 

![[htpasswd-oauth2-proxy-standalone-login.drawio.png]]

Traefik Config

OAuth2 Config

The Login page written in Your Preferrable language. 

The Cookie

## Final Thoughts

This solution eliminates Basic Authentication for your application using OAuth2 Proxy, making it ideal for newly developed software (Greenfield projects).

But what about the legacy devices and applications (Brownfield systems) in your network that have relied on Basic Authentication for decades? If you're still accessing them using Basic Authentication, your system is at significant risk.

How can these systems be protected? This is a critical topic with plenty to discuss, which we'll cover in detail in an upcoming [post](shielding-legacy-applications-eliminating-basic-authentication-without-code-changes)(coming soon). 