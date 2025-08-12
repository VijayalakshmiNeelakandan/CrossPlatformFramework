import XCTest

class SampleUITests: XCTestCase {
    func testExample() throws {
        let app = XCUIApplication()
        app.launch()
        XCTAssertTrue(app.buttons["Login"].exists)
    }
}