namespace Top.Serialization;

/// <summary>
/// Exception thrown when serialization fails due to cycles in the object graph.
/// </summary>
public class TopSerializationException : Exception
{
    public TopSerializationException(string message) : base(message) { }
    public TopSerializationException(string message, Exception inner) : base(message, inner) { }
}

/// <summary>
/// Exception thrown when deserialization fails due to invalid input.
/// </summary>
public class TopDeserializationException : Exception
{
    public TopDeserializationException(string message) : base(message) { }
    public TopDeserializationException(string message, Exception inner) : base(message, inner) { }
}
