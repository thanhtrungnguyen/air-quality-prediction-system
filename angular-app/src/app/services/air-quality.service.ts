import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AirQualityService {
  getAirQuality(): Observable<any> {
    const mockData = {
      index: 154,
      level: 'Unhealthy',
      mainPollutant: 'PM2.5',
      pollutants: [
        { name: 'PM2.5', concentration: 60, status: 'unhealthy' },
        { name: 'PM10', concentration: 72.6, status: 'moderate' },
        { name: 'O3', concentration: 16, status: 'good' },
        { name: 'NO2', concentration: 42, status: 'good' },
        { name: 'CO', concentration: 1112.9, status: 'good' },
      ],
      pm25Multiplier: 12,
    };

    return of(mockData);
  }
}
