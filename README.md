<h1 align="center">
  news-site-aws-api-gateway
</h1>
<p align="center">
AWS api gateway to serve data scrapped for <a href="https://github.com/rykumar13/react-news-website">react news website</a>
</p>
<h2>Purpose</h2>
<p>
Purpose of this api is to serve data for <a href="https://daily-roundup.netlify.app/">daily-roundup.netlify.app</a> website.
</p>
<br>
<h2> How it works</h2>
<p align="center">
  <ul>
  <li>Flask API is used to create a method that retrieves data from MySQL using mysql.connector library</li>
  <li>Zappa library is then used to deploy new builds from the command line</li>
  <li>Zappa settings file contains details needed to deploy this to AWS API Gateway</li>
  <li>This API supports HTTPS, Basic Auth & is CORS compliant</li>
  </ul>
  <br>
  <h2> Architecture Diagram</h2>
  <p>
  <img alt="diagram" src="https://raw.githubusercontent.com/rykumar13/react-news-website/4f574629a632a87e3cc2d86c6d9c21c73ccb330b/diagrams/diagram.svg" />
    <p>
</p>
<br>
<h2>
Technologies & Libraries used 🚀
  </h2>
  <p> 
    <ul>
     <li>React</li>
     <li>AWS RDS</li>
     <li>AWS EC2</li>
     <li>Flask API</li>
     <li>Zappa Library</li>
     <li>mysql.connector library</li>
    </ul>
  </p>
<h2>
  <br>
