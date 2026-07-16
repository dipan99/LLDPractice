import XCTest
@testable import VendingMachine

final class VendingMachineTests: XCTestCase {
    func makeMachine() -> VendingMachine {
        VendingMachine(slots: [
            "A1": Product(name: "Chips", priceInCents: 75, quantity: 2),
            "A2": Product(name: "Soda", priceInCents: 150, quantity: 1),
            "A3": Product(name: "Gum", priceInCents: 50, quantity: 0),
        ])
    }

    func testInsertCoinIncreasesBalance() {
        let machine = makeMachine()
        machine.insertCoin(.quarter)
        machine.insertCoin(.quarter)
        XCTAssertEqual(machine.insertedAmountInCents, 50)
    }

    func testSelectProductWithExactChangeDispenses() throws {
        let machine = makeMachine()
        machine.insertCoin(.quarter)
        machine.insertCoin(.quarter)
        machine.insertCoin(.quarter)

        let change = try machine.selectProduct(code: "A1")

        XCTAssertEqual(change, 0)
        XCTAssertEqual(machine.product(forCode: "A1")?.quantity, 1)
        XCTAssertEqual(machine.insertedAmountInCents, 0)
    }

    func testSelectProductReturnsCorrectChange() throws {
        let machine = makeMachine()
        machine.insertCoin(.dollarCoin)

        let change = try machine.selectProduct(code: "A1")

        XCTAssertEqual(change, 25)
        XCTAssertEqual(machine.insertedAmountInCents, 0)
    }

    func testSelectUnknownCodeThrows() {
        let machine = makeMachine()
        machine.insertCoin(.dollarCoin)

        XCTAssertThrowsError(try machine.selectProduct(code: "Z9"))
    }

    func testSelectOutOfStockProductThrows() {
        let machine = makeMachine()
        machine.insertCoin(.dollarCoin)

        XCTAssertThrowsError(try machine.selectProduct(code: "A3"))
    }

    func testSelectWithInsufficientFundsThrowsAndKeepsMoney() {
        let machine = makeMachine()
        machine.insertCoin(.quarter)

        XCTAssertThrowsError(try machine.selectProduct(code: "A2"))
        // the customer's money shouldn't vanish on a failed purchase
        XCTAssertEqual(machine.insertedAmountInCents, 25)
        XCTAssertEqual(machine.product(forCode: "A2")?.quantity, 1)
    }

    func testCancelTransactionRefundsAndResetsBalance() {
        let machine = makeMachine()
        machine.insertCoin(.quarter)
        machine.insertCoin(.dime)

        let refunded = machine.cancelTransaction()

        XCTAssertEqual(refunded, 35)
        XCTAssertEqual(machine.insertedAmountInCents, 0)
    }
}
