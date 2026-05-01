# BeautyVerse AI - Predictive & Personalized Salon Intelligence Platform

Full-stack demo platform with AI-driven beauty analysis, prediction, personalization, and salon analytics.

## Tech Stack
- Frontend: React + Vite + Tailwind CSS + Framer Motion + Recharts
- Backend: Node.js + Express
- Data: Mock JSON model storage

## Run
```bash
npm install
npm install --prefix client
npm install --prefix server
npm run dev
```

- Client: http://localhost:5173
- Server: http://localhost:5000

## Build Frontend
```bash
npm run build
```

## Key API Endpoints
- `POST /api/ai/analyze` -> mock skin analysis
- `GET /api/ai/future?days=30` -> future risk prediction
- `GET /api/beauty/dashboard` -> beauty score, issues, recommendations
- `GET /api/beauty/passport` -> history + milestones timeline
- `GET /api/beauty/routine?weather=Sunny` -> weather-based routine
- `GET /api/salon/analytics` -> admin dashboard chart data
