import { Injectable } from '@angular/core';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AirQualityService {
  getForecastData() {
    return of([
      {
        date: '2020-11-25',
        AQI: 154,
        co: 2162.93,
        no: 0.0,
        no2: 58.95,
        o3: 72.96,
        so2: 95.37,
        pm2_5: 346.73,
        pm10: 385.34,
        nh3: 9.37,
      },
      {
        date: '2020-11-26',
        AQI: 136,
        co: 2403.26,
        no: 0.02,
        no2: 78.83,
        o3: 58.65,
        so2: 123.98,
        pm2_5: 371.86,
        pm10: 412.33,
        nh3: 12.29,
      },
      {
        date: '2020-11-27',
        AQI: 161,
        co: 2883.91,
        no: 3.21,
        no2: 111.04,
        o3: 41.84,
        so2: 158.31,
        pm2_5: 421.5,
        pm10: 468.55,
        nh3: 17.48,
      },
    ]);
  }
}
