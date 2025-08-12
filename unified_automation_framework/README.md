# Unified Automation Framework

## Modules
- `python_playwright_web`: Web automation using Playwright + Mac resource monitoring.
- `ios_xcuitest_swift`: iOS automation using XCUITest.
- `android_espresso`: Android automation using Espresso.

## Pipeline Integration (Basic)
Use GitHub Actions or Jenkins to trigger tests for each platform using separate jobs for:
- Python (Playwright + resource monitoring)
- Xcode build and test (iOS)
- Gradle/Maven build and test (Android)