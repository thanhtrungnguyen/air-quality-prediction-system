// src/app/models/air-quality.model.ts
export interface Pollutant {
  name: string;
  value: number;
  unit: string;
  percentage: number;
}

export interface Recommendation {
  icon: string;
  text: string;
  link?: string;
}

export interface AirQuality {
  aqi: number;
  status: string;
  color: string;
  icon: string;
  pollutants: Pollutant[];
  recommendations: Recommendation[];
}
