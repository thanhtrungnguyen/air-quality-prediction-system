import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AirQualityService {
  private dataUrl = 'assets/air-quality.json';

  constructor(private http: HttpClient) { }

  getAirQualityData(): Observable<any[]> {
    return this.http.get<any[]>(this.dataUrl);
  }
}
