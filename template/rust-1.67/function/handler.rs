use axum::{Json, response::IntoResponse, http::StatusCode};
use axum::http::Request;

/// `handler()` is a valid Axum route handler.
/// You can use it like a classic handler in a Axum web application.
/// See https://github.com/tokio-rs/axum for more details.
pub async fn handler(req: Request<axum::body::Body>) -> impl IntoResponse {
    println!("Function invoked with method={} and path={}", req.method(), req.uri());

    (StatusCode::OK, Json("Hello, Rust runtime !"))
}