

<h1>FarmSense: AI-Powered Agricultural Advisory</h1>
<p>FarmSense is a full-stack, <strong>AI-powered</strong> platform designed to provide timely and actionable agricultural advice to Indian farmers. This MVP demonstrates a robust architecture integrating weather, mandi prices, and farmer-uploaded images to deliver intelligent, localized advisories. The application emphasizes simplicity, accessibility, and scalability with a modern, easy-to-deploy tech stack.</p>

<h2>Features</h2>
<p><strong>Weather Alerts:</strong> Fetches hyperlocal weather data to provide actionable alerts for activities like spraying and irrigation.</p>
<p><strong>Mandi Price Monitoring:</strong> Retrieves real-time and historical market prices from data.gov.in to aid selling decisions.</p>
<p><strong>Voice Interaction (ASR/TTS Stubs):</strong> Endpoints for a voice-based interface, enabling Hindi/English questions with audio responses.</p>
<p><strong>Pest &amp; Disease Reporting:</strong> Simple image upload for farmers to submit crop issue photos for review and advisory.</p>
<p><strong>Mobile-First Frontend:</strong> Lightweight, React-free HTML/JS frontend for a seamless mobile experience.</p>
<p><strong>Robust Backend:</strong> High-performance FastAPI backend handling business logic and API routing.</p>
<p><strong>Containerized Deployment:</strong> Entire stack containerized with Docker and orchestrated via Docker Compose for consistent environments.</p>

<h2>Technology Stack</h2>
<h3>Backend</h3>
<p><strong>Framework:</strong> FastAPI (Python)<br>
<strong>Dependencies:</strong> uvicorn, httpx, redis, pydantic</p>

<h3>Frontend</h3>
<p><strong>Technologies:</strong> HTML, CSS, Vanilla JavaScript (React-free)</p>

<h3>Database</h3>
<p><strong>Primary:</strong> PostgreSQL<br>
<strong>Cache:</strong> Redis</p>

<h3>Containerization</h3>
<p><strong>Orchestration:</strong> Docker Compose<br>
<strong>Containers:</strong> backend, nginx, db, redis</p>

<h3>Data Sources (External APIs)</h3>
<p>Ambee Agri Weather API<br>
data.gov.in Mandi Price API</p>

<h2>Project Structure</h2>
<pre>
.
├── backend/                  # Contains the FastAPI backend application
│   ├── app/                  # The core Python application
│   │   ├── logic/            # Business logic (e.g., advisory rules)
│   │   ├── routers/          # API endpoints
│   │   ├── services/         # Integrations with external APIs and caching
│   │   └── main.py           # Main FastAPI entry point
│   ├── Dockerfile            # Instructions to build the backend image
│   └── requirements.txt      # Python dependencies
├── frontend/                 # Contains the static frontend files
│   ├── index.html            # The main web page
│   └── script.js             # Frontend JavaScript logic
├── docker-compose.yml        # Defines and orchestrates all services
├── nginx.conf                # Nginx configuration for routing
└── README.md                 # This file
</pre>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<p>Install Docker Desktop (includes docker compose) to run this multi-container application easily.</p>

<h3>Step 1: Obtain API Keys</h3>
<p>The application requires two external API keys. Add them later to <code>docker-compose.yml</code>.</p>
<p><strong>Ambee Agri Weather API Key:</strong><br>
Visit the official Ambee API website, sign up for a free account, and get the key from the developer dashboard.</p>
<p><strong>data.gov.in Mandi Price API Key:</strong><br>
Go to the data.gov.in API portal, sign up, and receive the key via email.</p>

<h3>Step 2: Configure the Project</h3>
<p><strong>Clone the Repository:</strong></p>
<pre>
git clone [repository_url]
cd FarmSense
</pre>
<p><em>Note:</em> If this is not a real repository yet, create the files and folders manually as shown above.</p>
<p><strong>Add Your API Keys:</strong> Open <code>docker-compose.yml</code> and replace placeholders:</p>
<pre>
services:
  backend:
    environment:
      - AM_BEE_API_KEY=YOUR_AMBEE_API_KEY
      - DATA_GOV_API_KEY=YOUR_DATA_GOV_API_KEY
</pre>

<h3>Step 3: Run the Application</h3>
<p>From the project root, build and start all services:</p>
<pre>
docker-compose up
</pre>
<p>Run in detached mode:</p>
<pre>
docker-compose up -d
</pre>

<h3>Step 4: Access the App</h3>
<p>Open your browser at:</p>
<p><a href="http://localhost">http://localhost</a></p>
<p>The nginx container serves the <code>index.html</code> frontend and routes API calls to the FastAPI backend.</p>

<h3>Stopping the Application</h3>
<p>Stop and remove containers and their network:</p>
<pre>
docker-compose down
</pre>


[3](https://www.markdownguide.org/basic-syntax/)
[4](https://google.github.io/styleguide/docguide/style.html)
[5](https://github.com/orgs/community/discussions/109580)
[6](https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/)
[7](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
[8](https://stackoverflow.com/questions/14951321/how-to-display-html-content-in-github-readme-md)
