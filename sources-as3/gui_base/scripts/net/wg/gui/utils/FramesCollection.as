package net.wg.gui.utils
{
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import net.wg.data.constants.Errors;
   import net.wg.utils.IFramesCollection;
   
   public class FramesCollection implements IFramesCollection
   {
       
      
      private var _frames:Vector.<String> = null;
      
      private var _isDisposed:Boolean = false;
      
      public function FramesCollection(param1:MovieClip)
      {
         var _loc2_:FrameLabel = null;
         super();
         App.utils.asserter.assertNotNull(param1,Errors.CANT_NULL);
         this._frames = new Vector.<String>();
         for each(_loc2_ in param1.currentLabels)
         {
            this._frames.push(_loc2_.name);
         }
      }
      
      public function hasFrameLabel(param1:String) : Boolean
      {
         return this._frames.indexOf(param1) != -1;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this._frames.splice(0,this._frames.length);
         this._frames = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
   }
}
