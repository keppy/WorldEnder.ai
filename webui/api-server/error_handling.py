# see https://grpc.github.io/grpc/core/md_doc_statuscodes.html


# Base Exception for gRPC Canonical Error Codes
class CanonicalException(Exception):
    def __init__(self, message, status_code, details=None, resource=None):
        self.status_code = status_code
        self.resource = resource
        self.details = details or {}
        super().__init__(message)

    def __str__(self):
        base_message = super().__str__()
        if self.resource:
            return f"{base_message} (Resource: {self.resource})"
        return base_message


# Derived Exceptions


class OKException(CanonicalException):
    def __init__(
        self,
        message="Not actually an error; returned on success.",
        status_code=200,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class CancelledException(CanonicalException):
    def __init__(
        self,
        message="The operation was cancelled.",
        status_code=499,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class UnknownException(CanonicalException):
    def __init__(
        self,
        message="Unknown error. Typically a server error.",
        status_code=500,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class InvalidArgumentException(CanonicalException):
    def __init__(
        self,
        message="Client specified an invalid argument.",
        status_code=400,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class DeadlineExceededException(CanonicalException):
    def __init__(
        self,
        message="Deadline expired before the operation could complete.",
        status_code=504,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class NotFoundException(CanonicalException):
    def __init__(
        self,
        message="Some requested entity was not found.",
        status_code=404,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class AlreadyExistsException(CanonicalException):
    def __init__(
        self,
        message="Some entity that we attempted to create already exists.",
        status_code=409,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class PermissionDeniedException(CanonicalException):
    def __init__(
        self,
        message="Caller does not have permission to execute the specified operation.",
        status_code=403,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class ResourceExhaustedException(CanonicalException):
    def __init__(
        self,
        message="Some resource has been exhausted.",
        status_code=429,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class FailedPreconditionException(CanonicalException):
    def __init__(
        self,
        message="Operation was rejected because the system is not in a state required for the operation's execution.",
        status_code=400,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class AbortedException(CanonicalException):
    def __init__(
        self,
        message="The operation was aborted.",
        status_code=409,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class OutOfRangeException(CanonicalException):
    def __init__(
        self,
        message="Operation was attempted past the valid range.",
        status_code=400,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class UnimplementedException(CanonicalException):
    def __init__(
        self,
        message="Operation is not implemented or not supported/enabled.",
        status_code=501,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class InternalException(CanonicalException):
    def __init__(
        self,
        message="Internal server error.",
        status_code=500,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class UnavailableException(CanonicalException):
    def __init__(
        self,
        message="Service is currently unavailable.",
        status_code=503,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class DataLossException(CanonicalException):
    def __init__(
        self,
        message="Unrecoverable data loss or data corruption.",
        status_code=500,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)


class UnauthenticatedException(CanonicalException):
    def __init__(
        self,
        message="Request does not have valid authentication credentials.",
        status_code=401,
        details=None,
        resource=None,
    ):
        super().__init__(message, status_code, details, resource)
