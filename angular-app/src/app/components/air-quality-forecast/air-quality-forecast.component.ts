import { Component, OnInit } from '@angular/core';
import { AirQualityService } from '../../services/air-quality.service';

@Component({
  selector: 'app-air-quality-forecast',
  templateUrl: './air-quality-forecast.component.html',
  styleUrl: './air-quality-forecast.component.css'
})
export class AirQualityForecastComponent implements OnInit {
  forecast: any[] = [];
  selectedDetail: any = null;

  constructor(private airQualityService: AirQualityService) { }

  ngOnInit() {
    this.airQualityService.getForecastData().subscribe((data) => {
      this.forecast = data;
    });
  }

  selectDetail(detail: any) {
    this.selectedDetail = detail;
  }

  mapStatus(aqi: number) {
    switch (true) {
      case (aqi <= 50):
        return "Chất lượng không khí tốt";
      case (aqi > 50 && aqi <= 100):
        return "Chất lượng không khí chấp nhận được";
      case (aqi > 100 && aqi <= 200):
        return "Không tốt cho nhóm người có bệnh lý nền";
      case (aqi > 200 && aqi <= 300):
        return "Không tốt cho sức khoẻ";
      default:
        return "Rất nguy hại";
    }
  }
}
