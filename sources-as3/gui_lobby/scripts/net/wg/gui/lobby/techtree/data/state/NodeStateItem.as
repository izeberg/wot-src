package net.wg.gui.lobby.techtree.data.state
{
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class NodeStateItem implements IDisposable
   {
       
      
      private var _state:uint;
      
      private var _extState:uint;
      
      private var _props:StateProperties;
      
      private var _disposed:Boolean = false;
      
      public function NodeStateItem(param1:uint, param2:StateProperties, param3:uint = 1)
      {
         super();
         this._state = param1;
         this._props = param2;
         this._extState = param3;
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.onDispose();
      }
      
      public function getState() : uint
      {
         return this._state;
      }
      
      public function getExtState() : uint
      {
         return this._extState;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function resolveProps(param1:Object = null) : StateProperties
      {
         return this._props;
      }
      
      protected function onDispose() : void
      {
         if(this._props != null)
         {
            this._props.dispose();
            this._props = null;
         }
      }
   }
}
