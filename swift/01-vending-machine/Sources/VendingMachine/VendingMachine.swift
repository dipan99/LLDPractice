import Foundation

public enum Coin: Int, CaseIterable {
    case nickel = 5
    case dime = 10
    case quarter = 25
    case dollarCoin = 100

    public var valueInCents: Int { rawValue }
}

public struct Product {
    public let name: String
    public let priceInCents: Int
    public var quantity: Int

    public init(name: String, priceInCents: Int, quantity: Int) {
        self.name = name
        self.priceInCents = priceInCents
        self.quantity = quantity
    }
}

public final class VendingMachine {
    private var slots: [String: Product]
    private(set) public var insertedAmountInCents: Int = 0

    public init(slots: [String: Product]) {
        self.slots = slots
    }

    public func product(forCode code: String) -> Product? {
        slots[code]
    }

    public func insertCoin(_ coin: Coin) {
        insertedAmountInCents += coin.valueInCents
    }

    /// Select a product by its slot code and attempt to purchase it.
    ///
    /// TODO: handle all the cases described in the README —
    /// unknown code, out of stock, insufficient funds, and the
    /// successful path (decrement stock, compute change, reset the
    /// running total). Decide how each case should be signaled to
    /// the caller.
    public func selectProduct(code: String) throws -> Int {
        fatalError("TODO: implement product selection")
    }

    /// Cancel the current transaction.
    public func cancelTransaction() -> Int {
        let refund = insertedAmountInCents
        insertedAmountInCents = 0
        return refund
    }
}
