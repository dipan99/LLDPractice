// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "VendingMachine",
    targets: [
        .target(name: "VendingMachine"),
        .testTarget(name: "VendingMachineTests", dependencies: ["VendingMachine"]),
    ]
)
