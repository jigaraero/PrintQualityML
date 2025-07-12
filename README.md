# PrintQualityML

Python pipeline for real-time 3D print quality prediction and failure detection using sensor and camera data with ML and automated notifications.

## Project Overview

PrintQualityML is an intelligent 3D printing monitoring system that combines sensor data, computer vision, and machine learning to predict print quality and detect failures in real-time. The system aims to reduce material waste, save time, and improve overall 3D printing reliability by providing early warning of potential issues.

## Features

- **Real-time Monitoring**: Continuous analysis of print quality during the printing process
- **Multi-sensor Integration**: Combines temperature, vibration, and camera data for comprehensive monitoring
- **Machine Learning Prediction**: Uses trained models to predict print failures before they occur
- **Automated Notifications**: Sends alerts via email, SMS, or push notifications when issues are detected
- **Historical Analysis**: Tracks print quality trends over time
- **Configurable Thresholds**: Customizable sensitivity settings for different print materials and conditions

## Planned Architecture

### 1. Sensor Stream
- Temperature sensors (hotend, bed, ambient)
- Vibration/acceleration sensors
- Camera feed for visual inspection
- Filament flow rate monitoring
- Real-time data collection and preprocessing

### 2. Image Analysis
- Computer vision algorithms for defect detection
- Layer adhesion analysis
- Surface quality assessment
- Dimensional accuracy verification
- Feature extraction for ML input

### 3. ML Prediction
- Time series analysis for sensor data
- Convolutional Neural Networks (CNN) for image analysis
- Ensemble methods combining multiple data sources
- Real-time inference pipeline
- Continuous model improvement through feedback

### 4. Notification Automation
- Multi-channel alert system (email, SMS, push)
- Severity-based notification escalation
- Integration with printer control systems
- Automated print pause/stop capabilities
- Dashboard for monitoring multiple printers

## Basic Usage

```python
# Installation (planned)
pip install printqualityml

# Basic setup
from printqualityml import PrintMonitor

# Initialize monitor
monitor = PrintMonitor(
    camera_source='/dev/video0',
    temp_sensor_port='/dev/ttyUSB0',
    notification_config='config.yml'
)

# Start monitoring
monitor.start_monitoring()

# Configure alerts
monitor.set_alert_threshold('temperature', max_temp=250)
monitor.set_alert_threshold('quality_score', min_score=0.8)
```

## Contribution Guidelines

We welcome contributions from the community! Please follow these guidelines:

### Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Include unit tests for new features
- Maintain backward compatibility when possible

### Reporting Issues
- Use the GitHub issue tracker
- Provide detailed reproduction steps
- Include system information and logs
- Label issues appropriately

### Development Setup
```bash
# Clone the repository
git clone https://github.com/jigaraero/PrintQualityML.git
cd PrintQualityML

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap

- [ ] Core sensor integration framework
- [ ] Basic computer vision pipeline
- [ ] Initial ML model training
- [ ] Notification system implementation
- [ ] Web dashboard development
- [ ] Mobile app integration
- [ ] Multi-printer support
- [ ] Cloud-based analytics

## Support

For questions, issues, or contributions, please:
- Open an issue on GitHub
- Join our community discussions
- Check the documentation (coming soon)

---

*PrintQualityML - Making 3D printing more reliable, one layer at a time.*
